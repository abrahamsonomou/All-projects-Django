!function(e){"function"==typeof define&&define.amd?define(e):e()}((function(){"use strict";const e=e=>{"loading"===document.readyState?document.addEventListener("DOMContentLoaded",e):setTimeout(e,1)},a=e=>window.addEventListener("resize",e),t=e=>{const a=e.replace(/[-_\s.]+(.)?/g,((e,a)=>a?a.toUpperCase():""));return`${a.substr(0,1).toLowerCase()}${a.substr(1)}`},o=(e,a)=>{try{return JSON.parse(e.dataset[t(a)])}catch(o){return e.dataset[t(a)]}},n=(e,a=document.documentElement)=>getComputedStyle(a).getPropertyValue(`--phoenix-${e}`).trim(),l=(e,a,t=864e5)=>{const o=(a-e)/t;return Array.from({length:o+1},((a,o)=>new Date(e.valueOf()+t*o)))},{merge:i}=window._,r=(e,a,t)=>{console.log(i(t(),a)),e.setOption(i(t(),a))},s=(e,a="MMM DD")=>{let t="";return e.forEach((e=>{t+=`<div class='ms-1'>\n        <h6 class="text-700"><span class="fas fa-circle me-1 fs--2" style="color:${e.borderColor?e.borderColor:e.color}"></span>\n          ${e.seriesName} : ${"object"==typeof e.value?e.value[1]:e.value}\n        </h6>\n      </div>`})),`<div>\n            <p class='mb-2 text-600'>\n              ${window.dayjs(e[0].axisValue).isValid()?window.dayjs(e[0].axisValue).format(a):e[0].axisValue}\n            </p>\n            ${t}\n          </div>`},{echarts:c}=window,d=["January","February","March","April","May","June","July","August","September","October","November","December"],g=[{lat:53.958332,long:-1.080278,name:"Diana Meyer",street:"Slude Strand 27",location:"1130 Kobenhavn"},{lat:52.958332,long:-1.080278,name:"Diana Meyer",street:"Slude Strand 27",location:"1130 Kobenhavn"},{lat:51.958332,long:-1.080278,name:"Diana Meyer",street:"Slude Strand 27",location:"1130 Kobenhavn"},{lat:53.958332,long:-1.080278,name:"Diana Meyer",street:"Slude Strand 27",location:"1130 Kobenhavn"},{lat:54.958332,long:-1.080278,name:"Diana Meyer",street:"Slude Strand 27",location:"1130 Kobenhavn"},{lat:55.958332,long:-1.080278,name:"Diana Meyer",street:"Slude Strand 27",location:"1130 Kobenhavn"},{lat:53.908332,long:-1.080278,name:"Diana Meyer",street:"Slude Strand 27",location:"1130 Kobenhavn"},{lat:53.008332,long:-1.080278,name:"Diana Meyer",street:"Slude Strand 27",location:"1130 Kobenhavn"},{lat:53.158332,long:-1.080278,name:"Diana Meyer",street:"Slude Strand 27",location:"1130 Kobenhavn"},{lat:53.000032,long:-1.080278,name:"Diana Meyer",street:"Slude Strand 27",location:"1130 Kobenhavn"},{lat:52.292001,long:-2.22,name:"Anke Schroder",street:"Industrivej 54",location:"4140 Borup"},{lat:52.392001,long:-2.22,name:"Anke Schroder",street:"Industrivej 54",location:"4140 Borup"},{lat:51.492001,long:-2.22,name:"Anke Schroder",street:"Industrivej 54",location:"4140 Borup"},{lat:51.192001,long:-2.22,name:"Anke Schroder",street:"Industrivej 54",location:"4140 Borup"},{lat:52.292001,long:-2.22,name:"Anke Schroder",street:"Industrivej 54",location:"4140 Borup"},{lat:54.392001,long:-2.22,name:"Anke Schroder",street:"Industrivej 54",location:"4140 Borup"},{lat:51.292001,long:-2.22,name:"Anke Schroder",street:"Industrivej 54",location:"4140 Borup"},{lat:52.102001,long:-2.22,name:"Anke Schroder",street:"Industrivej 54",location:"4140 Borup"},{lat:52.202001,long:-2.22,name:"Anke Schroder",street:"Industrivej 54",location:"4140 Borup"},{lat:51.063202,long:-1.308,name:"Tobias Vogel",street:"Mollebakken 33",location:"3650 Olstykke"},{lat:51.363202,long:-1.308,name:"Tobias Vogel",street:"Mollebakken 33",location:"3650 Olstykke"},{lat:51.463202,long:-1.308,name:"Tobias Vogel",street:"Mollebakken 33",location:"3650 Olstykke"},{lat:51.563202,long:-1.308,name:"Tobias Vogel",street:"Mollebakken 33",location:"3650 Olstykke"},{lat:51.763202,long:-1.308,name:"Tobias Vogel",street:"Mollebakken 33",location:"3650 Olstykke"},{lat:51.863202,long:-1.308,name:"Tobias Vogel",street:"Mollebakken 33",location:"3650 Olstykke"},{lat:51.963202,long:-1.308,name:"Tobias Vogel",street:"Mollebakken 33",location:"3650 Olstykke"},{lat:51.000202,long:-1.308,name:"Tobias Vogel",street:"Mollebakken 33",location:"3650 Olstykke"},{lat:51.000202,long:-1.308,name:"Tobias Vogel",street:"Mollebakken 33",location:"3650 Olstykke"},{lat:51.163202,long:-1.308,name:"Tobias Vogel",street:"Mollebakken 33",location:"3650 Olstykke"},{lat:52.263202,long:-1.308,name:"Tobias Vogel",street:"Mollebakken 33",location:"3650 Olstykke"},{lat:53.463202,long:-1.308,name:"Tobias Vogel",street:"Mollebakken 33",location:"3650 Olstykke"},{lat:55.163202,long:-1.308,name:"Tobias Vogel",street:"Mollebakken 33",location:"3650 Olstykke"},{lat:56.263202,long:-1.308,name:"Tobias Vogel",street:"Mollebakken 33",location:"3650 Olstykke"},{lat:56.463202,long:-1.308,name:"Tobias Vogel",street:"Mollebakken 33",location:"3650 Olstykke"},{lat:56.563202,long:-1.308,name:"Tobias Vogel",street:"Mollebakken 33",location:"3650 Olstykke"},{lat:56.663202,long:-1.308,name:"Tobias Vogel",street:"Mollebakken 33",location:"3650 Olstykke"},{lat:56.763202,long:-1.308,name:"Tobias Vogel",street:"Mollebakken 33",location:"3650 Olstykke"},{lat:56.863202,long:-1.308,name:"Tobias Vogel",street:"Mollebakken 33",location:"3650 Olstykke"},{lat:56.963202,long:-1.308,name:"Tobias Vogel",street:"Mollebakken 33",location:"3650 Olstykke"},{lat:57.973202,long:-1.308,name:"Tobias Vogel",street:"Mollebakken 33",location:"3650 Olstykke"},{lat:57.163202,long:-1.308,name:"Tobias Vogel",street:"Mollebakken 33",location:"3650 Olstykke"},{lat:51.163202,long:-1.308,name:"Tobias Vogel",street:"Mollebakken 33",location:"3650 Olstykke"},{lat:51.263202,long:-1.308,name:"Tobias Vogel",street:"Mollebakken 33",location:"3650 Olstykke"},{lat:51.363202,long:-1.308,name:"Tobias Vogel",street:"Mollebakken 33",location:"3650 Olstykke"},{lat:51.409,long:-2.647,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:53.68,long:-1.49,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:50.259998,long:-5.051,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:54.906101,long:-1.38113,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:53.383331,long:-1.466667,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:53.483002,long:-2.2931,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:51.509865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:51.109865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:51.209865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:51.309865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:51.409865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:51.609865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:51.709865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:51.809865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:51.909865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:52.109865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:52.209865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:52.309865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:52.409865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:52.509865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:52.609865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:52.709865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:52.809865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:52.909865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:52.519865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:52.529865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:52.539865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:53.549865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:52.549865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:53.109865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:53.209865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:53.319865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:53.329865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:53.409865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:53.559865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:53.619865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:53.629865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:53.639865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:53.649865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:53.669865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:53.669865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:53.719865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:53.739865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:53.749865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:53.759865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:53.769865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:53.769865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:53.819865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:53.829865,long:-.118092,name:"Richard Hendricks",street:"37 Seafield Place",location:"London"},{lat:53.483959,long:-2.244644,name:"Ethel B. Brooks",street:"2576 Sun Valley Road"},{lat:40.737,long:-73.923,name:"Marshall D. Lewis",street:"1489 Michigan Avenue",location:"Michigan"},{lat:39.737,long:-73.923,name:"Marshall D. Lewis",street:"1489 Michigan Avenue",location:"Michigan"},{lat:38.737,long:-73.923,name:"Marshall D. Lewis",street:"1489 Michigan Avenue",location:"Michigan"},{lat:37.737,long:-73.923,name:"Marshall D. Lewis",street:"1489 Michigan Avenue",location:"Michigan"},{lat:40.737,long:-73.923,name:"Marshall D. Lewis",street:"1489 Michigan Avenue",location:"Michigan"},{lat:41.737,long:-73.923,name:"Marshall D. Lewis",street:"1489 Michigan Avenue",location:"Michigan"},{lat:42.737,long:-73.923,name:"Marshall D. Lewis",street:"1489 Michigan Avenue",location:"Michigan"},{lat:43.737,long:-73.923,name:"Marshall D. Lewis",street:"1489 Michigan Avenue",location:"Michigan"},{lat:44.737,long:-73.923,name:"Marshall D. Lewis",street:"1489 Michigan Avenue",location:"Michigan"},{lat:45.737,long:-73.923,name:"Marshall D. Lewis",street:"1489 Michigan Avenue",location:"Michigan"},{lat:46.7128,long:74.006,name:"Elizabeth C. Lyons",street:"4553 Kenwood Place",location:"Fort Lauderdale"},{lat:40.7128,long:74.1181,name:"Elizabeth C. Lyons",street:"4553 Kenwood Place",location:"Fort Lauderdale"},{lat:14.235,long:51.9253,name:"Ralph D. Wylie",street:"3186 Levy Court",location:"North Reading"},{lat:15.235,long:51.9253,name:"Ralph D. Wylie",street:"3186 Levy Court",location:"North Reading"},{lat:16.235,long:51.9253,name:"Ralph D. Wylie",street:"3186 Levy Court",location:"North Reading"},{lat:14.235,long:51.9253,name:"Ralph D. Wylie",street:"3186 Levy Court",location:"North Reading"},{lat:15.8267,long:47.9218,name:"Hope A. Atkins",street:"3715 Hillcrest Drive",location:"Seattle"},{lat:15.9267,long:47.9218,name:"Hope A. Atkins",street:"3715 Hillcrest Drive",location:"Seattle"},{lat:23.4425,long:58.4438,name:"Samuel R. Bailey",street:"2883 Raoul Wallenberg Place",location:"Cheshire"},{lat:23.5425,long:58.3438,name:"Samuel R. Bailey",street:"2883 Raoul Wallenberg Place",location:"Cheshire"},{lat:-37.8927369333,long:175.4087452333,name:"Samuel R. Bailey",street:"3228 Glory Road",location:"Nashville"},{lat:-38.9064188833,long:175.4441556833,name:"Samuel R. Bailey",street:"3228 Glory Road",location:"Nashville"},{lat:-12.409874,long:-65.596832,name:"Ann J. Perdue",street:"921 Ella Street",location:"Dublin"},{lat:-22.090887,long:-57.411827,name:"Jorge C. Woods",street:"4800 North Bend River Road",location:"Allen"},{lat:-19.019585,long:-65.261963,name:"Russ E. Panek",street:"4068 Hartland Avenue",location:"Appleton"},{lat:-16.500093,long:-68.214684,name:"Russ E. Panek",street:"4068 Hartland Avenue",location:"Appleton"},{lat:-17.413977,long:-66.165321,name:"Russ E. Panek",street:"4068 Hartland Avenue",location:"Appleton"},{lat:-16.489689,long:-68.119293,name:"Russ E. Panek",street:"4068 Hartland Avenue",location:"Appleton"},{lat:54.766323,long:3.08603729,name:"Russ E. Panek",street:"4068 Hartland Avenue",location:"Appleton"},{lat:54.866323,long:3.08603729,name:"Russ E. Panek",street:"4068 Hartland Avenue",location:"Appleton"},{lat:49.537685,long:3.08603729,name:"Russ E. Panek",street:"4068 Hartland Avenue",location:"Appleton"},{lat:54.715424,long:.509207,name:"Russ E. Panek",street:"4068 Hartland Avenue",location:"Appleton"},{lat:44.891666,long:10.136665,name:"Russ E. Panek",street:"4068 Hartland Avenue",location:"Appleton"},{lat:48.078335,long:14.535004,name:"Russ E. Panek",street:"4068 Hartland Avenue",location:"Appleton"},{lat:-26.358055,long:27.398056,name:"Russ E. Panek",street:"4068 Hartland Avenue",location:"Appleton"},{lat:-29.1,long:26.2167,name:"Wilbur J. Dry",street:"2043 Jadewood Drive",location:"Northbrook"},{lat:-29.883333,long:31.049999,name:"Wilbur J. Dry",street:"2043 Jadewood Drive",location:"Northbrook"},{lat:-26.266111,long:27.865833,name:"Wilbur J. Dry",street:"2043 Jadewood Drive",location:"Northbrook"},{lat:-29.087217,long:26.154898,name:"Wilbur J. Dry",street:"2043 Jadewood Drive",location:"Northbrook"},{lat:-33.958252,long:25.619022,name:"Wilbur J. Dry",street:"2043 Jadewood Drive",location:"Northbrook"},{lat:-33.977074,long:22.457581,name:"Wilbur J. Dry",street:"2043 Jadewood Drive",location:"Northbrook"},{lat:-26.563404,long:27.844164,name:"Wilbur J. Dry",street:"2043 Jadewood Drive",location:"Northbrook"},{lat:51.21389,long:-102.462776,name:"Joseph B. Poole",street:"3364 Lunetta Street",location:"Wichita Falls"},{lat:52.321945,long:-106.584167,name:"Joseph B. Poole",street:"3364 Lunetta Street",location:"Wichita Falls"},{lat:50.288055,long:-107.793892,name:"Joseph B. Poole",street:"3364 Lunetta Street",location:"Wichita Falls"},{lat:52.7575,long:-108.28611,name:"Joseph B. Poole",street:"3364 Lunetta Street",location:"Wichita Falls"},{lat:50.393333,long:-105.551941,name:"Joseph B. Poole",street:"3364 Lunetta Street",location:"Wichita Falls"},{lat:50.930557,long:-102.807777,name:"Joseph B. Poole",street:"3364 Lunetta Street",location:"Wichita Falls"},{lat:52.856388,long:-104.610001,name:"Joseph B. Poole",street:"3364 Lunetta Street",location:"Wichita Falls"},{lat:52.289722,long:-106.666664,name:"Joseph B. Poole",street:"3364 Lunetta Street",location:"Wichita Falls"},{lat:52.201942,long:-105.123055,name:"Joseph B. Poole",street:"3364 Lunetta Street",location:"Wichita Falls"},{lat:53.278046,long:-110.00547,name:"Joseph B. Poole",street:"3364 Lunetta Street",location:"Wichita Falls"},{lat:49.13673,long:-102.990959,name:"Joseph B. Poole",street:"3364 Lunetta Street",location:"Wichita Falls"},{lat:45.484531,long:-73.597023,name:"Claudette D. Nowakowski",street:"3742 Farland Avenue",location:"San Antonio"},{lat:45.266666,long:-71.900002,name:"Claudette D. Nowakowski",street:"3742 Farland Avenue",location:"San Antonio"},{lat:45.349998,long:-72.51667,name:"Claudette D. Nowakowski",street:"3742 Farland Avenue",location:"San Antonio"},{lat:47.333332,long:-79.433334,name:"Claudette D. Nowakowski",street:"3742 Farland Avenue",location:"San Antonio"},{lat:45.400002,long:-74.033333,name:"Claudette D. Nowakowski",street:"3742 Farland Avenue",location:"San Antonio"},{lat:45.683334,long:-73.433334,name:"Claudette D. Nowakowski",street:"3742 Farland Avenue",location:"San Antonio"},{lat:48.099998,long:-77.783333,name:"Claudette D. Nowakowski",street:"3742 Farland Avenue",location:"San Antonio"},{lat:45.5,long:-72.316666,name:"Claudette D. Nowakowski",street:"3742 Farland Avenue",location:"San Antonio"},{lat:46.349998,long:-72.550003,name:"Claudette D. Nowakowski",street:"3742 Farland Avenue",location:"San Antonio"},{lat:48.119999,long:-69.18,name:"Claudette D. Nowakowski",street:"3742 Farland Avenue",location:"San Antonio"},{lat:45.599998,long:-75.25,name:"Claudette D. Nowakowski",street:"3742 Farland Avenue",location:"San Antonio"},{lat:46.099998,long:-71.300003,name:"Claudette D. Nowakowski",street:"3742 Farland Avenue",location:"San Antonio"},{lat:45.700001,long:-73.633331,name:"Claudette D. Nowakowski",street:"3742 Farland Avenue",location:"San Antonio"},{lat:47.68,long:-68.879997,name:"Claudette D. Nowakowski",street:"3742 Farland Avenue",location:"San Antonio"},{lat:46.716667,long:-79.099998,name:"299"},{lat:45.016666,long:-72.099998,name:"299"}],{echarts:m}=window,{L:h}=window;e((()=>{const e=document.querySelector(".echart-total-sales-chart"),t=l(new Date("5/1/2022"),new Date("5/30/2022"),864e5),i=[100,200,300,300,300,250,200,200,200,200,200,500,500,500,600,700,800,900,1e3,1100,850,600,600,600,400,200,200,300,300,300],s=[200,200,100,50,50,50,50,50,50,50,50,50,50,50,200,400,600,600,600,800,1e3,700,400,450,500,600,700,650,600,550],c=e=>{const a=window.dayjs(e[0].axisValue),t=window.dayjs(e[0].axisValue).subtract(1,"month"),o=e.map(((e,o)=>({value:e.value,date:o>0?t:a,color:e.color})));let n="";return o.forEach(((e,a)=>{n+=`<h6 class="fs--1 text-700 ${a>0&&"mb-0"}"><span class="fas fa-circle me-2" style="color:${e.color}"></span>\n      ${e.date.format("MMM DD")} : ${e.value}\n    </h6>`})),`<div class='ms-1'>\n              ${n}\n            </div>`};if(e){const l=o(e,"echarts"),d=window.echarts.init(e);r(d,l,(()=>({color:[n("primary"),n("info")],tooltip:{trigger:"axis",padding:10,backgroundColor:n("gray-100"),borderColor:n("gray-300"),textStyle:{color:n("dark")},borderWidth:1,transitionDuration:0,axisPointer:{type:"none"},formatter:c},xAxis:[{type:"category",data:t,axisLabel:{formatter:e=>window.dayjs(e).format("DD MMM"),interval:13,showMinLabel:!0,showMaxLabel:!1,color:n("gray-800"),align:"left",fontFamily:"Nunito Sans",fontWeight:600,fontSize:12.8},axisLine:{show:!0,lineStyle:{color:n("gray-200")}},axisTick:{show:!1},splitLine:{show:!0,interval:0,lineStyle:{color:n("gray-200")}},boundaryGap:!1},{type:"category",position:"bottom",data:t,axisLabel:{formatter:e=>window.dayjs(e).format("DD MMM"),interval:130,showMaxLabel:!0,showMinLabel:!1,color:n("gray-800"),align:"right",fontFamily:"Nunito Sans",fontWeight:600,fontSize:12.8},axisLine:{show:!1},axisTick:{show:!1},splitLine:{show:!1},boundaryGap:!1}],yAxis:{position:"right",axisPointer:{type:"none"},axisTick:"none",splitLine:{show:!1},axisLine:{show:!1},axisLabel:{show:!1}},series:[{name:"d",type:"line",data:i,showSymbol:!1,symbol:"circle"},{name:"e",type:"line",data:s,lineStyle:{type:"dashed",width:1,color:n("info")},showSymbol:!1,symbol:"circle"}],grid:{right:2,left:5,bottom:"20px",top:"2%",containLabel:!1},animation:!1}))),a((()=>{d.resize()}))}})),e((()=>{const e=document.querySelector(".echarts-new-customers");if(e){const t=o(e,"echarts"),i=window.echarts.init(e);r(i,t,(()=>({tooltip:{trigger:"item",padding:[7,10],backgroundColor:n("gray-100"),borderColor:n("gary-300"),textStyle:{color:n("dark")},borderWidth:1,transitionDuration:0},xAxis:[{type:"category",data:l(new Date("5/1/2022"),new Date("5/7/2022"),864e5),show:!0,boundaryGap:!1,axisLine:{show:!0,lineStyle:{color:n("gray-200")}},axisTick:{show:!1},axisLabel:{formatter:e=>window.dayjs(e).format("DD MMM"),showMinLabel:!0,showMaxLabel:!1,color:n("gray-800"),align:"left",interval:5,fontFamily:"Nunito Sans",fontWeight:600,fontSize:12.8}},{type:"category",position:"bottom",show:!0,data:l(new Date("5/1/2022"),new Date("5/7/2022"),864e5),axisLabel:{formatter:e=>window.dayjs(e).format("DD MMM"),interval:130,showMaxLabel:!0,showMinLabel:!1,color:n("gray-800"),align:"right",fontFamily:"Nunito Sans",fontWeight:600,fontSize:12.8},axisLine:{show:!1},axisTick:{show:!1},splitLine:{show:!1},boundaryGap:!1}],yAxis:{show:!1,type:"value",boundaryGap:!1},series:[{type:"line",data:[150,100,300,200,250,180,250],showSymbol:!1,symbol:"circle",lineStyle:{width:2,color:n("gray-200")},emphasis:{lineStyle:{color:n("gray-200")}}},{type:"line",data:[200,150,250,100,500,400,600],lineStyle:{width:2,color:n("primary")},showSymbol:!1,symbol:"circle"}],grid:{left:0,right:0,top:5,bottom:20}}))),a((()=>{i.resize()}))}})),e((()=>{const e=document.querySelector(".echart-top-coupons");if(e){const t=o(e,"options"),l=c.init(e);r(l,t,(()=>({color:[n("primary"),n("gray-200"),n("info")],tooltip:{trigger:"item",padding:[7,10],backgroundColor:n("gray-100"),borderColor:n("gray-300"),textStyle:{color:n("dark")},borderWidth:1,transitionDuration:0,formatter:e=>`<strong>${e.data.name}:</strong> ${e.percent}%`},legend:{show:!1},series:[{name:"72%",type:"pie",radius:["100%","87%"],avoidLabelOverlap:!1,emphasis:{scale:!1,itemStyle:{color:"inherit"}},itemStyle:{borderWidth:2,borderColor:n("white")},label:{show:!0,position:"center",formatter:"{a}",fontSize:23,color:n("dark")},data:[{value:72e5,name:"Percentage discount"},{value:18e5,name:"Fixed card discount"},{value:1e6,name:"Fixed product discount"}]}]}))),a((()=>{l.resize()}))}})),e((()=>{const e=document.querySelector(".echart-projection-actual"),t=(e=>{let a;switch(e){case"week":a=7;break;case"month":a=30;break;case"year":a=365;break;default:a=e}const t=new Date,o=t,n=new Date((new Date).setDate(t.getDate()-(a-1)));return l(n,o)})(10),i=[44485,20428,47302,45180,31034,46358,26581,36628,38219,43256],c=[38911,29452,31894,47876,31302,27731,25490,30355,27176,30393];if(e){const l=o(e,"echarts"),d=echarts.init(e);r(d,l,(()=>({color:[n("primary"),n("gray-300")],tooltip:{trigger:"axis",padding:[7,10],backgroundColor:n("gray-100"),borderColor:n("gray-300"),textStyle:{color:n("dark")},borderWidth:1,transitionDuration:0,axisPointer:{type:"none"},formatter:e=>s(e)},legend:{data:["Projected revenue","Actual revenue"],right:"right",width:"100%",itemWidth:16,itemHeight:8,itemGap:20,top:3,inactiveColor:n("gray-500"),textStyle:{color:n("gray-900"),fontWeight:600,fontFamily:"Nunito Sans"}},xAxis:{type:"category",axisLabel:{color:n("gray-800"),formatter:e=>window.dayjs(e).format("MMM DD"),interval:3,fontFamily:"Nunito Sans",fontWeight:600,fontSize:12.8},data:t,axisLine:{lineStyle:{color:n("gray-300")}},axisTick:!1},yAxis:{axisPointer:{type:"none"},axisTick:"none",splitLine:{interval:5,lineStyle:{color:n("gray-200")}},axisLine:{show:!1},axisLabel:{fontFamily:"Nunito Sans",fontWeight:600,fontSize:12.8,color:n("gray-800"),margin:20,verticalAlign:"bottom",formatter:e=>`$${e.toLocaleString()}`}},series:[{name:"Projected revenue",type:"bar",barWidth:"6px",data:c,barGap:"30%",label:{show:!1},itemStyle:{borderRadius:[2,2,0,0],color:n("primary")}},{name:"Actual revenue",type:"bar",data:i,barWidth:"6px",barGap:"30%",label:{show:!1},z:10,itemStyle:{borderRadius:[2,2,0,0],color:n("info-100")}}],grid:{right:0,left:3,bottom:0,top:"15%",containLabel:!0},animation:!1}))),a((()=>{d.resize()}))}})),e((()=>{const e=document.querySelector(".echart-returning-customer");if(e){const t=o(e,"echarts"),l=m.init(e);r(l,t,(()=>({color:n("gray-100"),legend:{data:[{name:"Fourth time",icon:"roundRect",itemStyle:{color:n("primary-300"),borderWidth:0}},{name:"Third time",icon:"roundRect",itemStyle:{color:n("info-200"),borderWidth:0}},{name:"Second time",icon:"roundRect",itemStyle:{color:n("primary"),borderWidth:0}}],right:"right",width:"100%",itemWidth:16,itemHeight:8,itemGap:20,top:3,inactiveColor:n("gray-500"),inactiveBorderWidth:0,textStyle:{color:n("gray-900"),fontWeight:600,fontFamily:"Nunito Sans"}},tooltip:{trigger:"axis",axisPointer:{type:"none"},padding:[7,10],backgroundColor:n("gray-100"),borderColor:n("gray-300"),textStyle:{color:n("dark")},borderWidth:1,transitionDuration:0,formatter:s},xAxis:{type:"category",data:d,show:!0,boundaryGap:!1,axisLine:{show:!0,lineStyle:{color:n("gray-300")}},axisTick:{show:!1},axisLabel:{showMinLabel:!1,showMaxLabel:!1,color:n("gray-800"),formatter:e=>e.slice(0,3),fontFamily:"Nunito Sans",fontWeight:600,fontSize:12.8},splitLine:{show:!0,lineStyle:{color:n("gray-200"),type:"dashed"}}},yAxis:{type:"value",boundaryGap:!1,axisLabel:{showMinLabel:!0,showMaxLabel:!0,color:n("gray-800"),formatter:e=>`${e}%`,fontFamily:"Nunito Sans",fontWeight:600,fontSize:12.8},splitLine:{show:!0,lineStyle:{color:n("gray-200")}}},series:[{name:"Fourth time",type:"line",data:[62,90,90,90,78,84,17,17,17,17,82,95],showSymbol:!1,symbol:"circle",symbolSize:10,emphasis:{lineStyle:{width:1}},lineStyle:{type:"dashed",width:1,color:n("primary-300")},itemStyle:{borderColor:n("primary-300"),borderWidth:3}},{name:"Third time",type:"line",data:[50,50,30,62,18,70,70,22,70,70,70,70],showSymbol:!1,symbol:"circle",symbolSize:10,emphasis:{lineStyle:{width:1}},lineStyle:{width:1,color:n("info-200")},itemStyle:{borderColor:n("info-200"),borderWidth:3}},{name:"Second time",type:"line",data:[40,78,60,78,60,20,60,40,60,40,20,78],showSymbol:!1,symbol:"circle",symbolSize:10,emphasis:{lineStyle:{width:3}},lineStyle:{width:3,color:n("primary")},itemStyle:{borderColor:n("primary"),borderWidth:3}}],grid:{left:0,right:8,top:"14%",bottom:0,containLabel:!0}}))),a((()=>{l.resize()}))}})),e((()=>{const e=document.getElementById("payingCustomerChart");e&&((e,a)=>{if(!e)return;const t=e.getContext("2d");t&&new window.Chart(t,a())})(e,(()=>({type:"doughnut",data:{labels:["Paying","Non-paying"],datasets:[{data:[30,70],backgroundColor:[n("primary"),n("primary-100")],borderColor:[n("primary"),n("primary-100")],borderRadius:[{outerStart:15,outerEnd:0,innerStart:15,innerEnd:0},{outerStart:0,outerEnd:15,innerStart:0,innerEnd:15}]}]},options:{tooltips:{backgroundColor:n("primary-100"),borderColor:n("primary-100"),borderWidth:1,titleColor:n("black"),position:"nearest",callbacks:{labelTextColor:()=>n("black")}},rotation:-90,circumference:"180",cutout:"80%",plugins:{legend:{display:!1}}}})))})),e((()=>{const e=document.getElementById("map");if(h&&e){const e="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",a=h.tileLayer(e),t=h.map("map",{center:h.latLng(25.659195,30.182691),zoom:.6,layers:[a],minZoom:1.4}),o=h.markerClusterGroup({chunkedLoading:!1,spiderfyOnMaxZoom:!1});g.map((e=>{const{name:a,location:t,street:n}=e,l=h.icon({iconUrl:"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAApCAYAAADAk4LOAAAACXBIWXMAAAFgAAABYAEg2RPaAAADpElEQVRYCZ1XS1LbQBBtybIdiMEJKSpUqihgEW/xDdARyAnirOIl3MBH8NK7mBvkBpFv4Gy9IRSpFIQiRPyNfqkeZkY9HwmFt7Lm06+7p/vN2MmyDIrQ6QebALAHAD4AbFuWfQeAAACGs5H/w5jlsJJw4wMA+GhMFuMA99jIDJJOP+ihZwDQFmNuowWO1wS3viDXpdEdZPEc0odruj0EgN5s5H8tJOEEX8R3rbkMtcU34NTqhe5nSQTJ7Tkk80s6/Gk28scGiULguFBffgdufdEwWoQ0uoXo8hdAlooVH0REjISfwZSlyHGh0V5n6aHAtKTxXI5g6nQnMH0P4bEgwtR18Yw8Pj8QZ4ARUAI0Hl+fQZZGisGEBVwHr7XKzox57DXZ/ij8Cdwe2u057z9/wygOxRl4S2vSUHx1oucaMQGAHTrgtdag9mK5aN+Wx/uAAQ9Zenp/SRce4TpaNbQK4+sTcGqeTB/aIXv3XN5oj2VKqii++U0JunpZ8urxee4hvjqVc2hHpBDXuKKT9XMgVYJ1/1fPGSeaikzgmWWkMIi9bVf8UhotXxzORn5gWFchI8QyttlzjS0qpsaIGY2MMsujV/AUSdcY0dDpB6/EiOPYzclR1CI5mOez3ekHvrFLxa7cR5pTscfrXjk0Vhm5V2PqLUWnH3R5GbPGpMVD7E1ckXesKBQ7AS/vmQ1c0+kHuxpBj98lTCm8pbc5QRJRdZ6qHb/wGryXq3Lxszv+5gySuwvxueXySwYvHEjuQ9ofTGKYlrmK1EsCHMd5SoD7mZ1HHFCBHLNbMEshvrugqWLn01hpVVJhFgVGkDvK7hR6n2B+d9C7xsqWsbkqHv4cCsWezEb+o2SR+SFweUBxfA5wH7kShjKt2vWL57Px3GhIFEezkb8pxvUWHYhotAfCk2AtkEcxoOttrxUWDR5svb1emSQKj0WXK1HYIgFREbiBqmoZcB2RkbE+byMZiosorVgAZF1ID7yQhEs38wa7nUqNDezdlavC2HbBGSQkGgZ8uJVBmzeiKCRRpEa9ilWghORVeGB7BxeSKF5xqbFBkxBrFKUk/JHA7ppENQaCnCjthK+3opCEYyANztXmZN858cDYWSUSHk3A311GAZDvo6deNKUk1EsqnJoQlkYBNlmxQZeaMgmxoUokICoHDce351RCCiuKoirJWEgNOYvQplM2VCLhUqF7jf94rW9kHVUjQeheV4riv0i4ZOzzz/2y/+0KAOAfr4EE4HpCFhwAAAAASUVORK5CYII="}),i=h.marker([e.lat,e.long],{icon:l}),r=`\n        <h6 class="mb-1">${a}</h6>\n        <p class="m-0 text-500">${n}, ${t}</p>\n      `,s=h.popup({minWidth:180}).setContent(r);return i.bindPopup(s),o.addLayer(i),!0})),t.addLayer(o)}}))}));