import { Component, OnInit, Inject, Input } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';

@Component({
  selector: 'bro-food-form',
  templateUrl: './food-form.component.html',
  styleUrls: ['./food-form.component.scss']
})
export class FoodFormComponent {
  minDate = new Date();
  maxDate = new Date().setDate(this.minDate.getDate() + 7);
  constructor(
    private dialogRef: MatDialogRef<FoodFormComponent>,
    @Inject(MAT_DIALOG_DATA) public data: FoodProduct
  ) {}

  startUpload(event: FileList) {
    // The File object
    const file = event.item(0);
    console.log(file);
  }
}
