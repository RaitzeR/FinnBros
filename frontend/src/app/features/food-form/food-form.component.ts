import { Component, OnInit, Inject, Input } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { BehaviorSubject } from 'rxjs/BehaviorSubject';
import {
  DomSanitizer,
  SafeResourceUrl,
  SafeUrl
} from '@angular/platform-browser';

@Component({
  selector: 'bro-food-form',
  templateUrl: './food-form.component.html',
  styleUrls: ['./food-form.component.scss']
})
export class FoodFormComponent implements OnInit {
  minDate = new Date();
  maxDate = new Date().setDate(this.minDate.getDate() + 7);
  // State for dropzone CSS toggling
  isHovering: boolean;
  bgStyle: string;
  constructor(
    private dialogRef: MatDialogRef<FoodFormComponent>,
    private san: DomSanitizer,
    @Inject(MAT_DIALOG_DATA) public data: FoodProduct
  ) {
    const sanit = this.san.bypassSecurityTrustUrl(this.data.image_url);
    this.bgStyle = `linear-gradient(rgba(255, 192, 203, 0.5), pink), url(${
      this.data.image_url
    }) center center/cover no-repeat`;
  }

  toggleHover(event: boolean) {
    this.isHovering = event;
  }

  startUpload(event: FileList) {
    // The File object
    const file = event.item(0);
    console.log(file);
  }

  onSubmit(form) {
    console.log(form);
  }

  ngOnInit() {}
}
