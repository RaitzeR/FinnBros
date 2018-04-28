import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { FindViewRoutingModule } from './find-view-routing.module';
import { FindViewComponent } from './find-view.component';
import { FoodsListModule } from '@features/foods-list/foods-list.module';
import { MapModule } from '@features/map/map.module';

@NgModule({
  imports: [CommonModule, FindViewRoutingModule, FoodsListModule, MapModule],
  declarations: [FindViewComponent]
})
export class FindViewModule {}
