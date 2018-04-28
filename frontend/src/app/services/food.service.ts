import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs/BehaviorSubject';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class FoodService {
  private foodsList = new BehaviorSubject<foodProduct[]>([]);
  constructor(private http: HttpClient) {
    console.log('init foodz');
    fetch(
      'https://us-central1-mockdatshit.cloudfunctions.net/mockdatshii/2MdejmhGpppmLlimVDQN?token=lJX77PyKzgb7k17Iht5gyXMSgG33'
    )
      .then(res => res.json())
      .then(foodsJson => {
        /*
        const parsed = JSON.parse(foodsJson) as any[];
        const mapped: foodProduct[] = parsed.map(item => {
          return item.fields;
        });
        */
        this.foodsList.next(foodsJson);
      })
      .catch(e => console.error(e));
  }
  public getFood(): BehaviorSubject<foodProduct[]> {
    return this.foodsList;
  }

  public dispatchNewFoodItem() {
    this.http
      .post('https://finnbros-foodapp.herokuapp.com/create_food_post/', '', {
        params: { title: 'jussiRuokaa' }
      })
      .subscribe(res => console.log(res));
  }
}
