import { Component, OnInit } from '@angular/core';
import { FoodService } from '../../services/food.service';
import { BehaviorSubject } from 'rxjs/BehaviorSubject';

@Component({
  selector: 'bro-foods-list',
  templateUrl: './foods-list.component.html',
  styleUrls: ['./foods-list.component.scss']
})
export class FoodsListComponent implements OnInit {
  public foodList = new BehaviorSubject<foodProduct[]>([]);

  constructor(private foodService: FoodService) {}

  ngOnInit() {
    this.foodList = this.foodService.getFood();
  }

  dispatchNewFoodItem() {
    this.foodService.dispatchNewFoodItem();
  }
}
