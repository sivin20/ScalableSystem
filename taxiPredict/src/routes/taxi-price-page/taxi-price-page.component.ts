import { Component } from '@angular/core';
import {TaxiPriceService} from "../../services/taxi-price.service";
import {RouterLink} from "@angular/router";
import {FormsModule} from "@angular/forms";

interface day {
  id: number,
  day: string,
}

interface details {
  day: number,
  time: number,
  weather: string
}
@Component({
  selector: 'app-taxi-price-page',
  standalone: true,
  imports: [
    RouterLink,
    FormsModule
  ],
  templateUrl: './taxi-price-page.component.html',
  styleUrl: './taxi-price-page.component.scss'
})
export class TaxiPricePageComponent {

  price: string = '-'

  days: day[] = [
    {id: 1, day: 'Monday'},
    {id: 2, day: 'Tuesday'},
    {id: 3, day: 'Wednesday'},
    {id: 4, day: 'Thursday'},
    {id: 5, day: 'Friday'},
    {id: 6, day: 'Saturday'},
    {id: 7, day: 'Sunday'}
  ]

  weathers: string[] = [
    'clear',
    'sunny',
    'rain'
  ]

  inputDetails: details = {
    day: 0,
    time: 0,
    weather: ''
  }
  constructor (
    public taxiPriceService: TaxiPriceService, // used in html
  ) {}

  submitForm(form: any): void {
    if (form.valid) {
      console.log('Form data:', this.inputDetails);
      this.getPrice(this.inputDetails)
    }
  }
  async getPrice(details: details) {
    const params: string = `weekday=${details.day}&time=${details.time}&weather=${details.weather}`
    this.price = (await this.taxiPriceService.getPrice(params)).price.toFixed(2)
  }
}
