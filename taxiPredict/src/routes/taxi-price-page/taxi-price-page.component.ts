import {Component, OnInit} from '@angular/core';
import {TaxiPriceService} from "../../services/taxi-price.service";
import {RouterLink} from "@angular/router";
import {FormBuilder, FormsModule, ReactiveFormsModule, Validators} from "@angular/forms";

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
    FormsModule,
    ReactiveFormsModule
  ],
  templateUrl: './taxi-price-page.component.html',
  styleUrl: './taxi-price-page.component.scss'
})
export class TaxiPricePageComponent implements OnInit {

  price: string = '-'

  priceForm: any

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
  constructor (
    public taxiPriceService: TaxiPriceService,
    private formBuilder: FormBuilder
  ) {}

  ngOnInit(): void {
    this.priceForm = this.formBuilder.group({
      day: [null, Validators.required],
      time: [null, [Validators.required]],
      weather: [null, Validators.required],
    });
  }

  submitForm(): void {
    if (this.priceForm.valid) {
      const details = {
        day: this.priceForm.value.day,
        time: this.priceForm.value.time,
        weather: this.priceForm.value.weather
      }
      this.getPrice(details)
    } else {
      console.log("not valid")
    }
  }
  async getPrice(details: details) {
    const params: string = `weekday=${details.day}&time=${details.time}&weather=${details.weather}`
    this.price = (await this.taxiPriceService.getPrice(params)).price.toFixed(2)
  }
}
