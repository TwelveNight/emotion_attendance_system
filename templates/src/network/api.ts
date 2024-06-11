import axios from 'axios'

class FaceApi {
    http = axios.create({
        baseURL: 'http://127.0.0.1:8088'
    });
    urls = {
        register: '/register',
        checkIn:'check_in',
        checkOut: 'check_out',
        recognize: '/recognize',
        unregister: '/unregister',
        terminate: '/terminate',

    }
    
    async checkIn(value:string){
        console.log(value)
        return await this.http.post(this.urls.checkIn,{model_type:value})
    }
    
    async register(username:string){
        return await this.http.post(this.urls.register,{username})
    }
}

const faceApi = new FaceApi()

export default faceApi