import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MapComponent } from './map.component';
import { AgmCoreModule } from '@agm/core';
import { environment } from '@env/environment';
import { FoodProductModalComponent } from './food-product-modal/food-product-modal.component';
import { MatDialogModule } from '@angular/material/dialog';
import { MapService } from '@features/map/map.service';
import { MatChipsModule, MatButtonModule } from '@angular/material';

@NgModule({
  imports: [
    CommonModule,
    AgmCoreModule.forRoot({
      apiKey: environment.googleMapsKey
    }),
    MatDialogModule,
    MatChipsModule,
    MatButtonModule
  ],
  declarations: [MapComponent, FoodProductModalComponent],
  providers: [MapService],
  exports: [MapComponent],
  bootstrap: [FoodProductModalComponent]
})
export class MapModule {}
