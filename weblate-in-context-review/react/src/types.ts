export interface OccurrenceIdentity {
  project: string;
  component: string;
  language: string;
  context: string;
}

export interface Occurrence extends OccurrenceIdentity {
  id: string;
  element: HTMLElement;
}

export interface TargetBinding {
  unit_id: number;
  content_hash: number;
  web_url: string;
}

export interface ReviewUnit {
  binding: {
    context: string;
    targets: Record<string, TargetBinding>;
  };
  unit: {
    source: string[];
    target: string[];
    state: number;
  };
}
