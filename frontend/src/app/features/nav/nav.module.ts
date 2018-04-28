import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NavComponent } from './nav.component';
import { RouterModule } from '@angular/router';
import { MatButtonModule } from '@angular/material';

@NgModule({
  imports: [CommonModule, RouterModule, MatButtonModule],
  declarations: [NavComponent],
  exports: [NavComponent],
  bootstrap: [NavComponent]
})
export class NavModule {}
