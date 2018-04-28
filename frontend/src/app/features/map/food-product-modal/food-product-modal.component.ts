import { Component, OnInit, Inject } from '@angular/core';
import {
  MatDialogRef,
  MAT_DIALOG_DATA,
  MatDialog
} from '@angular/material/dialog';
import { BehaviorSubject } from 'rxjs/BehaviorSubject';
import { FoodFormComponent } from '@features/food-form/food-form.component';

@Component({
  selector: 'bro-food-product-modal',
  templateUrl: './food-product-modal.component.html',
  styleUrls: ['./food-product-modal.component.scss']
})
export class FoodProductModalComponent {
  constructor(
    private dialog: MatDialog,
    private dialogRef: MatDialogRef<FoodProductModalComponent>,
    @Inject(MAT_DIALOG_DATA) public data: FoodProduct
  ) {}

  editThisModal() {
    const expiresAsDate = new Date(this.data.expires);
    console.log(expiresAsDate);

    const dataModifiedDate = {
      ...this.data,
      expires: expiresAsDate
    };
    this.dialog.open(FoodFormComponent, {
      data: this.data,
      panelClass: 'modalAsForm'
    });
  }
}
