import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material';
import { FoodFormComponent } from '@features/food-form/food-form.component';
import { AuthService } from '../../services/auth.service';
import { Observable } from 'rxjs/Observable';

@Component({
  selector: 'bro-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.scss']
})
export class NavComponent implements OnInit {
  public user: Observable<User>;
  constructor(private dialog: MatDialog, private auth: AuthService) {
    this.user = auth.getUser();
  }

  ngOnInit() {}

  public newFoodListning(): void {
    const newFoodProduct: FoodProduct = {
      title: '',
      categories: ['Food'],
      expires: new Date(),
      latitude: undefined,
      longitude: undefined,
      createdAt: new Date(),
      street_address: '',
      city: '',
      image_url: ''
    };
    this.dialog.open(FoodFormComponent, {
      data: newFoodProduct,
      panelClass: 'modalAsForm'
    });
  }

  public logout() {
    this.auth.signOut();
  }
}
