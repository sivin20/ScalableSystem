import { Component } from '@angular/core';
import {TaxiPriceService} from "../../services/taxi-price.service";

interface day {
  id: number,
  day: string,
}
@Component({
  selector: 'app-taxi-price-page',
  standalone: true,
  imports: [],
  templateUrl: './taxi-price-page.component.html',
  styleUrl: './taxi-price-page.component.scss'
})
export class TaxiPricePageComponent {

  price: number = 10

  days: day[] = [
    {id: 1, day: 'Monday'},
    {id: 2, day: 'Tuesday'},
    {id: 3, day: 'Wednesday'},
    {id: 4, day: 'Thursday'},
    {id: 5, day: 'Friday'},
    {id: 6, day: 'Saturday'},
    {id: 7, day: 'Sunday'}
  ]
  constructor (
    public taxiPriceService: TaxiPriceService, // used in html
  ) {}

  async test() {
    this.price = await this.taxiPriceService.getPrice()
  }
}
