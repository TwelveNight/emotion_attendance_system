import {FC, useCallback, useState} from "react";
import css from "./app.module.css";
import { Button, Input, Select } from "antd";
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
  const checkIn = useCallback(async ()=>{
    const response = await faceApi.checkIn(checkInValue)
    console.log(response)
  },[checkInValue])
  
  const renderLeft = useCallback(() => {
    return (
      <div className={css.leftBox}>
        <div className={css.formBox}>
          <div className={css.checkBox}>
              <p>录入模式:</p>
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
              <Button type="primary" onClick={checkIn}>开始录入</Button>
          </div>
          <div className={css.checkBox}>
              <p>录出模式:</p>
              <Select
                style={{
                  width: 100,
                }}
                defaultValue={"pkl"}
                options={[
                  { label: "pkl", value: "pkl" },
                  { label: "deepface", value: "deepface" },
                  { label: "h5", value: "h5" },
                ]}
              ></Select>
              <Button type="primary">开始录出</Button>
          </div>
          <div className={css.registerBox}>
            <Input placeholder="输入你的用户名"></Input>
            <Button type="primary">注册</Button>
          </div>
        </div>
      </div>
    );
  }, []);
  
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
      <h1 className={css.leftTitle}>人脸识别系统</h1>
      <div className={css.container}>
        {renderLeft()}
        {renderImage()}
        <RightStatus name="叶墨沫" isSmile={true} isUnique={true}></RightStatus>
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
