import html2canvas from "html2canvas";
import { Camera, ExternalLink, Languages, MessageSquare, X } from "lucide-react";
import { useEffect, useState } from "react";
import { createPortal } from "react-dom";
import { useReviewContext } from "./ReviewContext";
import type { Occurrence, ReviewUnit } from "./types";
import "./review-overlay.css";

function reviewPath(gatewayUrl: string, occurrence: Occurrence) {
  const path = [
    occurrence.project,
    occurrence.component,
    occurrence.language,
    occurrence.context,
  ]
    .map(encodeURIComponent)
    .join("/");
  return `${gatewayUrl.replace(/\/$/, "")}/v1/review/${path}`;
}

function screenshotPath(gatewayUrl: string, occurrence: Occurrence) {
  const path = [
    occurrence.project,
    occurrence.component,
    occurrence.language,
    occurrence.context,
  ]
    .map(encodeURIComponent)
    .join("/");
  return `${gatewayUrl.replace(/\/$/, "")}/v1/screenshots/${path}`;
}

function commentPath(gatewayUrl: string, occurrence: Occurrence) {
  const path = [
    occurrence.project,
    occurrence.component,
    occurrence.language,
    occurrence.context,
  ]
    .map(encodeURIComponent)
    .join("/");
  return `${gatewayUrl.replace(/\/$/, "")}/v1/comments/${path}`;
}

async function captureAnnotatedScreenshot(occurrence: Occurrence) {
  const canvas = await html2canvas(document.documentElement, {
    backgroundColor: "#ffffff",
    height: document.documentElement.scrollHeight,
    ignoreElements: (element) => element.classList.contains("wl-review-layer"),
    logging: false,
    scale: 1,
    useCORS: true,
    width: document.documentElement.scrollWidth,
    windowHeight: document.documentElement.scrollHeight,
    windowWidth: document.documentElement.scrollWidth,
  });
  const rectangle = occurrence.element.getBoundingClientRect();
  const context = canvas.getContext("2d");
  if (!context) throw new Error("Unable to annotate screenshot");

  const padding = 8;
  const x = rectangle.left + window.scrollX - padding;
  const y = rectangle.top + window.scrollY - padding;
  const width = rectangle.width + padding * 2;
  const height = rectangle.height + padding * 2;
  context.save();
  context.lineJoin = "round";
  context.strokeStyle = "#ffffff";
  context.lineWidth = 10;
  context.strokeRect(x, y, width, height);
  context.strokeStyle = "#d9272e";
  context.lineWidth = 5;
  context.strokeRect(x, y, width, height);
  context.restore();

  return new Promise<Blob>((resolve, reject) => {
    canvas.toBlob((blob) => {
      if (blob) resolve(blob);
      else reject(new Error("Unable to encode screenshot"));
    }, "image/png");
  });
}

export function ReviewOverlay() {
  const { gatewayUrl, reviewToken, occurrences } = useReviewContext();
  const [enabled, setEnabled] = useState(true);
  const [selected, setSelected] = useState<Occurrence | null>(null);
  const [reviewUnit, setReviewUnit] = useState<ReviewUnit | null>(null);
  const [error, setError] = useState("");
  const [commentOpen, setCommentOpen] = useState(false);
  const [comment, setComment] = useState("");
  const [commentStatus, setCommentStatus] = useState("");
  const [submittingComment, setSubmittingComment] = useState(false);
  const [captureStatus, setCaptureStatus] = useState("");
  const [capturing, setCapturing] = useState(false);
  const [, refreshPositions] = useState(0);

  useEffect(() => {
    const refresh = () => refreshPositions((value) => value + 1);
    window.addEventListener("resize", refresh);
    window.addEventListener("scroll", refresh, true);
    return () => {
      window.removeEventListener("resize", refresh);
      window.removeEventListener("scroll", refresh, true);
    };
  }, []);

  useEffect(() => {
    if (!selected) {
      setReviewUnit(null);
      setError("");
      setCommentOpen(false);
      setComment("");
      setCommentStatus("");
      setCaptureStatus("");
      return;
    }
    const controller = new AbortController();
    setReviewUnit(null);
    setError("");
    fetch(reviewPath(gatewayUrl, selected), {
      headers: { Authorization: `Bearer ${reviewToken}` },
      signal: controller.signal,
    })
      .then(async (response) => {
        if (!response.ok) throw new Error(await response.text());
        return response.json() as Promise<ReviewUnit>;
      })
      .then(setReviewUnit)
      .catch((reason: Error) => {
        if (reason.name !== "AbortError") setError(reason.message);
      });
    return () => controller.abort();
  }, [gatewayUrl, reviewToken, selected]);

  const submitComment = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (!selected || !comment.trim()) return;
    setSubmittingComment(true);
    setCommentStatus("");
    try {
      const response = await fetch(commentPath(gatewayUrl, selected), {
        method: "POST",
        headers: {
          Authorization: `Bearer ${reviewToken}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ comment: comment.trim() }),
      });
      if (!response.ok) throw new Error(await response.text());
      setComment("");
      setCommentOpen(false);
      setCommentStatus("Comment added to Weblate.");
    } catch (reason) {
      const message = reason instanceof Error ? reason.message : String(reason);
      setCommentStatus(`Unable to add comment: ${message}`);
    } finally {
      setSubmittingComment(false);
    }
  };

  const uploadScreenshot = async () => {
    if (!selected) return;
    setCapturing(true);
    setCaptureStatus("");
    try {
      const image = await captureAnnotatedScreenshot(selected);
      const formData = new FormData();
      formData.append("image", image, `${selected.context}.png`);
      const response = await fetch(screenshotPath(gatewayUrl, selected), {
        method: "POST",
        headers: { Authorization: `Bearer ${reviewToken}` },
        body: formData,
      });
      if (!response.ok) throw new Error(await response.text());
      setCaptureStatus("Screenshot added to Weblate.");
    } catch (reason) {
      const message = reason instanceof Error ? reason.message : String(reason);
      setCaptureStatus(`Unable to add screenshot: ${message}`);
    } finally {
      setCapturing(false);
    }
  };

  return createPortal(
    <div className="wl-review-layer" aria-label="Translation review mode">
      <button
        className="wl-review-mode-toggle"
        onClick={() => {
          setEnabled((current) => !current);
          setSelected(null);
        }}
        aria-label={enabled ? "Pause review mode" : "Start review mode"}
        aria-pressed={enabled}
        title={enabled ? "Pause review mode" : "Start review mode"}
      >
        <Languages aria-hidden="true" />
      </button>
      {enabled && occurrences.map((occurrence) => {
        const rectangle = occurrence.element.getBoundingClientRect();
        return (
          <button
            key={occurrence.id}
            className="wl-review-marker"
            style={{
              top: rectangle.top,
              left: rectangle.left,
              width: rectangle.width,
              height: rectangle.height,
            }}
            onClick={() => setSelected(occurrence)}
            aria-label={`Review ${occurrence.context}`}
            title={`Review ${occurrence.context}`}
          />
        );
      })}
      {enabled && selected && (
        <aside className="wl-review-panel" aria-label="Translation details">
          <header>
            <Languages aria-hidden="true" />
            <div>
              <p>In-context review</p>
              <h2>{selected.context}</h2>
            </div>
            <button
              className="wl-review-icon-button"
              onClick={() => setSelected(null)}
              aria-label="Close translation details"
              title="Close"
            >
              <X aria-hidden="true" />
            </button>
          </header>
          {error && <p className="wl-review-error">Unable to load: {error}</p>}
          {!error && !reviewUnit && <p className="wl-review-loading">Loading...</p>}
          {reviewUnit && (
            <div className="wl-review-content">
              <section>
                <span>Source</span>
                <p>{reviewUnit.unit.source.join(" | ")}</p>
              </section>
              <section>
                <span>Translation</span>
                <p>{reviewUnit.unit.target.join(" | ") || "Not translated"}</p>
              </section>
              <dl>
                <div>
                  <dt>Unit</dt>
                  <dd>{reviewUnit.binding.targets[selected.language].unit_id}</dd>
                </div>
                <div>
                  <dt>State</dt>
                  <dd>{reviewUnit.unit.state}</dd>
                </div>
              </dl>
              <a
                className="wl-review-command"
                href={reviewUnit.binding.targets[selected.language].web_url}
                target="_blank"
                rel="noreferrer"
              >
                Open in Weblate <ExternalLink aria-hidden="true" />
              </a>
              <button
                className="wl-review-command wl-review-secondary-command"
                onClick={() => {
                  setCommentOpen((current) => !current);
                  setCommentStatus("");
                }}
                aria-expanded={commentOpen}
              >
                <MessageSquare aria-hidden="true" />
                Add comment to Weblate
              </button>
              {commentOpen && (
                <form className="wl-review-comment-form" onSubmit={submitComment}>
                  <label htmlFor="wl-review-comment">Comment</label>
                  <textarea
                    id="wl-review-comment"
                    value={comment}
                    onChange={(event) => setComment(event.target.value)}
                    maxLength={1000}
                    rows={4}
                    required
                    autoFocus
                  />
                  <div>
                    <button
                      type="button"
                      onClick={() => {
                        setCommentOpen(false);
                        setComment("");
                      }}
                      disabled={submittingComment}
                    >
                      Cancel
                    </button>
                    <button
                      type="submit"
                      disabled={submittingComment || !comment.trim()}
                    >
                      {submittingComment ? "Submitting..." : "Submit"}
                    </button>
                  </div>
                </form>
              )}
              {commentStatus && (
                <p className="wl-review-action-status" role="status">
                  {commentStatus}
                </p>
              )}
              <button
                className="wl-review-command wl-review-secondary-command"
                onClick={uploadScreenshot}
                disabled={capturing}
              >
                <Camera aria-hidden="true" />
                {capturing ? "Uploading screenshot..." : "Add screenshot to Weblate"}
              </button>
              {captureStatus && (
                <p className="wl-review-action-status" role="status">
                  {captureStatus}
                </p>
              )}
            </div>
          )}
        </aside>
      )}
    </div>,
    document.body,
  );
}
