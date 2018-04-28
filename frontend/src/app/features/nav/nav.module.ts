import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NavComponent } from './nav.component';
import { RouterModule } from '@angular/router';
import { MatButtonModule, MatDialogModule } from '@angular/material';
import { FoodFormModule } from '@features/food-form/food-form.module';

@NgModule({
  imports: [
    CommonModule,
    RouterModule,
    MatButtonModule,
    FoodFormModule,
    MatDialogModule
  ],
  declarations: [NavComponent],
  exports: [NavComponent],
  bootstrap: [NavComponent]
})
export class NavModule {}
