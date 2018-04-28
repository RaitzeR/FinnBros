/* SystemJS module definition */
declare var module: NodeModule;
interface NodeModule {
  id: string;
}

interface User {
  email: string;
  uid?: string;
}

interface foodProduct {
  title: string;
}
