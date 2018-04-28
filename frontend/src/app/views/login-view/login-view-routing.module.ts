import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginViewComponent } from './login-view.component';

const routes: Routes = [
  {
    path: '',
    pathMatch: 'full',
    component: LoginViewComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class LoginViewRoutingModule {}
