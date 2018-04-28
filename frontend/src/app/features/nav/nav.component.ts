import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material';
import { FoodFormComponent } from '@features/food-form/food-form.component';

@Component({
  selector: 'bro-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.scss']
})
export class NavComponent implements OnInit {
  constructor(private dialog: MatDialog) {}

  ngOnInit() {}

  public newFoodListning(): void {
    const newFoodProduct: FoodProduct = {
      title: '',
      categories: ['Food'],
      expires: new Date(),
      latitude: undefined,
      longitude: undefined,
      createdAt: new Date(),
      street_address: '',
      city: '',
      image_url: ''
    };
    this.dialog.open(FoodFormComponent, {
      data: newFoodProduct,
      panelClass: 'modalAsForm'
    });
  }
}
