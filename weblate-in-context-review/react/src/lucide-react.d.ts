declare module "lucide-react" {
  import type {
    ForwardRefExoticComponent,
    RefAttributes,
    SVGProps,
  } from "react";

  type Icon = ForwardRefExoticComponent<
    SVGProps<SVGSVGElement> & RefAttributes<SVGSVGElement>
  >;

  export const ExternalLink: Icon;
  export const CloudOff: Icon;
  export const Camera: Icon;
  export const Home: Icon;
  export const Languages: Icon;
  export const LogIn: Icon;
  export const LogOut: Icon;
  export const MessageSquare: Icon;
  export const Minus: Icon;
  export const Plus: Icon;
  export const Settings: Icon;
  export const X: Icon;
}
