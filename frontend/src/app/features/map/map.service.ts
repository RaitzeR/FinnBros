import { Injectable } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { FoodProductModalComponent } from '@features/map/food-product-modal/food-product-modal.component';
import { BehaviorSubject } from 'rxjs/BehaviorSubject';

@Injectable()
export class MapService {
  private lat = new BehaviorSubject<number>(46.009079);
  private lng = new BehaviorSubject<number>(8.956816);
  private zoom = new BehaviorSubject<number>(14);

  constructor(private dialog: MatDialog) {}

  public showFoodProductDialog(product: FoodProduct) {
    this.dialog.open(FoodProductModalComponent, {
      data: product
    });
    this.lat.next(product.latitude);
    this.lng.next(product.longitude);
  }

  public getCoordinates() {
    return {
      lat: this.lat,
      lng: this.lng
    };
  }

  public getZoom() {
    return this.zoom;
  }
}
