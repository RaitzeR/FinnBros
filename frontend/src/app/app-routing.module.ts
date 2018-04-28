import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [
  {
    path: '',
    pathMatch: 'full',
    loadChildren: '@views/landing-view/landing-view.module#LandingViewModule'
  },
  {
    path: 'login',
    loadChildren: '@views/login-view/login-view.module#LoginViewModule'
  },
  {
    path: 'find',
    loadChildren: '@views/find-view/find-view.module#FindViewModule'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
