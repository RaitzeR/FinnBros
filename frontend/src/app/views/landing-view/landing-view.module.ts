import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { LandingViewRoutingModule } from './landing-view-routing.module';
import { LandingViewComponent } from './landing-view.component';

@NgModule({
  imports: [CommonModule, LandingViewRoutingModule],
  declarations: [LandingViewComponent]
})
export class LandingViewModule {}
