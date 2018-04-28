import { Component, OnInit, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { BehaviorSubject } from 'rxjs/BehaviorSubject';

@Component({
  selector: 'bro-food-product-modal',
  templateUrl: './food-product-modal.component.html',
  styleUrls: ['./food-product-modal.component.scss']
})
export class FoodProductModalComponent {
  constructor(
    private dialogRef: MatDialogRef<FoodProductModalComponent>,
    @Inject(MAT_DIALOG_DATA) public data: FoodProduct
  ) {}
}
