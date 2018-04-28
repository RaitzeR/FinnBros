import { Component, OnInit, Inject } from '@angular/core';
import {
  MatDialogRef,
  MAT_DIALOG_DATA,
  MatDialog
} from '@angular/material/dialog';
import { BehaviorSubject } from 'rxjs/BehaviorSubject';
import { FoodFormComponent } from '@features/food-form/food-form.component';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
  selector: 'bro-food-product-modal',
  templateUrl: './food-product-modal.component.html',
  styleUrls: ['./food-product-modal.component.scss']
})
export class FoodProductModalComponent {
  bgStyle: string;
  constructor(
    private dialog: MatDialog,
    private san: DomSanitizer,
    private dialogRef: MatDialogRef<FoodProductModalComponent>,
    @Inject(MAT_DIALOG_DATA) public data: FoodProduct
  ) {
    const sanit = this.san.bypassSecurityTrustUrl(this.data.image_url);
    this.bgStyle = `linear-gradient(rgba(0, 0, 0, 0.25), rgba(0, 0, 0, 0.75)), url(${
      this.data.image_url
    }) center center/cover no-repeat`;
  }

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
