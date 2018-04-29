/* SystemJS module definition */
declare var module: NodeModule;
interface NodeModule {
  id: string;
}

interface User {
  email: string;
  uid?: string;
}

interface FoodProduct {
  title: string;
  categories: string[];
  createdAt: Date;
  expires: Date;
  latitude: number;
  longitude: number;
  street_address: string;
  city: string;
  image_url: string;
}
