import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LandingViewComponent } from './landing-view.component';

const routes: Routes = [
  {
    path: '',
    pathMatch: 'full',
    component: LandingViewComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class LandingViewRoutingModule {}
