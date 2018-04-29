import { Component, OnInit } from '@angular/core';
import { BehaviorSubject } from 'rxjs/BehaviorSubject';
import { FoodService } from 'app/services/food.service';
import { MapService } from '@features/map/map.service';
import { mapStyle } from '@features/map/mapStyle';

@Component({
  selector: 'bro-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.scss']
})
export class MapComponent implements OnInit {
  public lat = new BehaviorSubject<number>(46.009079);
  public lng = new BehaviorSubject<number>(8.956816);
  public zoom = new BehaviorSubject<number>(14);

  public foodList = new BehaviorSubject<FoodProduct[]>([]);
  public mapStyle = mapStyle;

  constructor(
    private foodService: FoodService,
    private mapService: MapService
  ) {
    this.lat = mapService.getCoordinates().lat;
    this.lng = mapService.getCoordinates().lng;
    this.zoom = mapService.getZoom();
  }

  handleMarkerClick(product: FoodProduct) {
    console.log('click: ', product);
    this.mapService.showFoodProductDialog(product);
  }

  ngOnInit() {
    this.foodList = this.foodService.getFood();
    this.foodList.subscribe(x => console.log(x));
  }
}
