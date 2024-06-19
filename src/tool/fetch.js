//该函数将token（jwt令牌）加入请求头并发送至后端封装成一个函数
//deliver(url,data)传入url(请求发送目标，例如myVariablelogin")
// 和data(发送数据，如{name: '6512', email: '758439675'})
//返回后端返回数据
export let vid = "https://2w513euuq12k.ngrok.xiaomiqiu123.top";
if(localStorage.getItem("yes")==="1"){
    vid="http://localhost:8080";
}
export function Fetch(url, data, Method) {
    let token = localStorage.getItem('token');
    if (!token) {
        localStorage.setItem('token', "");//保存jwt
        // localStorage.setItem('login',"no");//保存jwt
        token = localStorage.getItem('token');
    }
    url=vid+url;
    return fetch(url, {
        method: Method,
        headers: {
            'Content-Type': 'application/json',
            'Authorization': '' + token,
        },
        body: JSON.stringify(data),
    }).then(response => {
            if (!response.ok) {
                // 如果响应的状态码不是2xx，那么就抛出一个错误
                return response.json().then(json => {
                    throw new Error(json.message);
                });
            }
            // alert(response.json().toString());
            return response.json();
        });
}
export function GetFetch(url, Method) {
    let token = localStorage.getItem('token');
    if (!token) {
        localStorage.setItem('token', "");//保存jwt
        token = localStorage.getItem('token');
    }
    url=vid+url;
    return fetch(url, {
        method: Method,
        headers: {
            'Content-Type': 'application/json',
            'Authorization': '' + token,
        },
    }).then(response => {
        if (!response.ok) {
            // 如果响应的状态码不是2xx，那么就抛出一个错误
            return response.json().then(json => {
                throw new Error(json.message);
            });
        }
        // alert(response.json().toString());
        return response.json();
    });
}
