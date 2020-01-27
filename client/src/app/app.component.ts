import { Component,OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import {throwError} from 'rxjs'; 
import { ParametertypeService } from './services/master/parametertype.service';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'client';
  constructor(private parametertype:ParametertypeService,private http: HttpClient) { 
  }

  ngOnInit() {
    this.parametertype.getCon().subscribe(data => {
      console.log(data);
    })
    // let s = this.http.get('api/parametertype/');
    // const localUrl = 'assets/data/smartphone.json';
    // return this.http.get(localUrl);

    // console.log(s);
  }
}
