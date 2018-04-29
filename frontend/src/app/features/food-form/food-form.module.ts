import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FoodFormComponent } from './food-form.component';
import {
  MatDialogModule,
  MatInputModule,
  MatDatepickerModule,
  MatNativeDateModule,
  MatChipsModule,
  MatButtonModule
} from '@angular/material';
import { FormsModule } from '@angular/forms';

@NgModule({
  imports: [
    CommonModule,
    MatDialogModule,
    MatInputModule,
    FormsModule,
    MatDatepickerModule,
    MatNativeDateModule,
    MatChipsModule,
    MatButtonModule
  ],
  declarations: [FoodFormComponent],
  exports: [FoodFormComponent],
  bootstrap: [FoodFormComponent]
})
export class FoodFormModule {}
