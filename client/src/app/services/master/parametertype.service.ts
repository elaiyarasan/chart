import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ParametertypeService {

  constructor(private http: HttpClient) { }
  getCon(){
    return this.http.get('api/parametertype')
  }
}
