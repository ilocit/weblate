import {
  createContext,
  type PropsWithChildren,
  useContext,
  useEffect,
  useRef,
  useState,
} from "react";
import type { Occurrence, OccurrenceIdentity } from "./types";

interface ReviewContextValue {
  gatewayUrl: string;
  reviewToken: string;
  occurrences: Occurrence[];
  register: (element: HTMLElement, identity: OccurrenceIdentity) => () => void;
}

const ReviewContext = createContext<ReviewContextValue | null>(null);

export interface ReviewProviderProps extends PropsWithChildren {
  gatewayUrl: string;
  reviewToken: string;
}

export function ReviewProvider({
  gatewayUrl,
  reviewToken,
  children,
}: ReviewProviderProps) {
  const nextId = useRef(0);
  const [occurrences, setOccurrences] = useState<Occurrence[]>([]);

  const register = (element: HTMLElement, identity: OccurrenceIdentity) => {
    const occurrence = {
      ...identity,
      element,
      id: `l10n-occurrence-${nextId.current++}`,
    };
    setOccurrences((current) => [...current, occurrence]);
    return () =>
      setOccurrences((current) =>
        current.filter((candidate) => candidate.id !== occurrence.id),
      );
  };

  return (
    <ReviewContext.Provider
      value={{ gatewayUrl, reviewToken, occurrences, register }}
    >
      {children}
    </ReviewContext.Provider>
  );
}

export function useReviewContext() {
  const context = useContext(ReviewContext);
  if (!context) throw new Error("Review components require ReviewProvider");
  return context;
}

export function L10nOccurrence({
  identity,
  children,
}: PropsWithChildren<{ identity: OccurrenceIdentity }>) {
  const reference = useRef<HTMLSpanElement>(null);
  const { register } = useReviewContext();

  useEffect(() => {
    if (!reference.current) return;
    return register(reference.current, identity);
  }, [identity.component, identity.context, identity.language, identity.project]);

  return (
    <span
      ref={reference}
      data-l10n-project={identity.project}
      data-l10n-component={identity.component}
      data-l10n-language={identity.language}
      data-l10n-key={identity.context}
    >
      {children}
    </span>
  );
}
