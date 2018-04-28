import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FoodsListComponent } from './foods-list.component';
import { MatCardModule } from '@angular/material';

@NgModule({
  imports: [CommonModule, MatCardModule],
  declarations: [FoodsListComponent],
  exports: [FoodsListComponent]
})
export class FoodsListModule {}
