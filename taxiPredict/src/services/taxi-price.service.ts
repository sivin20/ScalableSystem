import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";


@Injectable({
	providedIn: 'root'
})
export class TaxiPriceService {

  private BACKEND_URL: string = 'http://127.0.0.1:8000'

	constructor(
		private http: HttpClient,

	) { }


	async getPrice(params: string): Promise<{price: number}> {
		return new Promise(async (resolve: any, reject: any) => {
      const url: string =`${this.BACKEND_URL}/price?${params}`
			return this.http.get(url).toPromise().then((res) => {
				return resolve(res)
			}).catch((err) => {
				return reject(err);
			})
		})
	}
}
