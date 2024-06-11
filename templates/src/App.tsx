import {FC, useCallback, useState} from "react";
import css from './app.module.css';
import { Button, Input, Select, message } from "antd";
import RightStatus from "./components/RightStatus/RightStatus";
import StatusTable from "./components/StatusTable/StatusTable";
import faceApi from "./network/api";
const mockUserStatusInfoList:UserStatusInfoType[] = [
  {
    name: "叶墨沫",
    times: "2021-09-01",
    isSmile: true,
    emotions: true,
  },
  {
    name: "叶墨沫",
    times: "2021-09-01",
    isSmile: true,
    emotions: true,
  },
  {
    name: "叶墨沫",
    times: "2021-09-01",
    isSmile: true,
    emotions: true,
  },
  {
    name: "叶墨沫",
    times: "2021-09-01",
    isSmile: true,
    emotions: true,
  },
  {
    name: "叶墨沫",
    times: "2021-09-01",
    isSmile: true,
    emotions: true,
  },
  {
    name: "叶墨沫",
    times: "2021-09-01",
    isSmile: true,
    emotions: true,
  },
  {
    name: "叶墨沫",
    times: "2021-09-01",
    isSmile: true,
    emotions: true,
  },
  {
    name: "叶墨沫",
    times: "2021-09-01",
    isSmile: true,
    emotions: true,
  },
  {
    name: "叶墨沫",
    times: "2021-09-01",
    isSmile: true,
    emotions: true,
  },
     {
    name: "叶墨沫",
    times: "2021-09-01",
    isSmile: true,
    emotions: true,
  },
  {
    name: "叶墨沫",
    times: "2021-09-01",
    isSmile: true,
    emotions: true,
  },
  {
    name: "叶墨沫",
    times: "2021-09-01",
    isSmile: true,
    emotions: true,
  },
  {
    name: "叶墨沫",
    times: "2021-09-01",
    isSmile: true,
    emotions: true,
  },
]

const App: FC = () => {
  const [checkInValue,setCheckInValue] = useState('pkl')
  const [registerUsername,setRegisterUsername] = useState('')
  const [emotion,setEmotion] = useState('未知')
  const [userId, setUserId] = useState('')
  const [frame,setFrame] = useState('')
  const [messageApi,messageHolader] = message.useMessage()
  const [isUnique , setIsUnique] = useState(false)
  const checkIn = useCallback(async ()=>{
    messageApi.loading({
      content:'加载中',
      duration: 0,
    })
    try{
      const response = await faceApi.checkIn(checkInValue)
      messageApi.destroy()
    if (response.status == 200){
      if (response.data.code == 5){
        messageApi.error({
            content:'录入失败,用户未注册',
            duration:3
        })
        setIsUnique(false)
        setFrame('data:image/jpeg;base64,'+ response.data.frame)
        return
      }
      if (response.data.code == 4){
        messageApi.error({
            content:'录入失败，未识别到人脸',
            duration:3
        })
        setIsUnique(false)
        return
      }
      //返回为text类型
      messageApi.success({
        
        content:`录入成功,表情:${response.data.emotion}`, 
        duration:3
      })
      setIsUnique(true)
      setEmotion(response.data.emotion)
      setUserId(response.data.user_id)
      setFrame('data:image/jpeg;base64,'+ response.data.frame)
      
    }else{
      messageApi.error('录入失败')
    }
    }catch(e){
      messageApi.destroy()
      messageApi.error('录入失败')
    }
  },[checkInValue])
  
  const register = async ()=>{
    messageApi.loading({
      content:'加载中',
      duration: 0,
    })
    const promise =await faceApi.register(registerUsername)
    messageApi.destroy()
  }
  
  const renderLeft = useCallback(() => {
    return (
      <div className={css.leftBox}>
        <div className={css.formBox}>
          <div className={css.checkBox}>
              <p>打卡模式:</p>
              <Select
                style={{
                  width: 100,
                }}
                defaultValue={checkInValue}
                onChange={(value)=>{
                    setCheckInValue(value)
                }}
                options={[
                  { label: "pkl", value: "pkl" },
                  { label: "deepface", value: "deepface" },
                  { label: "h5", value: "h5" },
                ]}
              ></Select>
              <Button type="primary" onClick={checkIn}>打卡</Button>
          </div>
          <div className={css.registerBox}>
            <Input placeholder="输入你的用户名" onChange={(e)=>{
              console.log(e.target.value)
              setRegisterUsername(e.target.value)
            }}></Input>
            <Button type="primary" onClick={register}>注册</Button>
          </div>
        </div>
      </div>
    );
  }, [registerUsername,checkInValue])
  
  const renderImage = useCallback(() => {
    return (
      <div className={css.rightBox}>
        <div style={{
          borderRadius:'20px',
          overflow:'hidden',
        }}>
          <img src="http://127.0.0.1:8088/video_feed" width="800px" height="600px"></img>
        </div>
      </div>
    );
  }, []);


  return (
    <div className={css.allBox}>
      {messageHolader}
      <h1 className={css.leftTitle}>人脸识别系统</h1>
      <div className={css.container}>
        {renderLeft()}
        {renderImage()}
        <RightStatus name={userId}  isUnique={isUnique} emotion={emotion} frame={frame}></RightStatus>
      </div>
      <div style={{
        width:'100%'
      }}>
        <StatusTable userStatusInfoList={mockUserStatusInfoList}></StatusTable>
      </div>
    </div>
  );
};
export default App;
