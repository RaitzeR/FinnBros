import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { FindViewRoutingModule } from './find-view-routing.module';
import { FindViewComponent } from './find-view.component';
import { FoodsListModule } from '@features/foods-list/foods-list.module';

@NgModule({
  imports: [CommonModule, FindViewRoutingModule, FoodsListModule],
  declarations: [FindViewComponent]
})
export class FindViewModule {}
