import { FC, useCallback } from "react";
import css from "./app.module.css";
import { Button, Input, Select } from "antd";
import RightStatus from "./components/RightStatus/RightStatus";
const App: FC = () => {
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
                defaultValue={"pkl"}
                options={[
                  { label: "pkl", value: "pkl" },
                  { label: "deepface", value: "deepface" },
                  { label: "h5", value: "h5" },
                ]}
              ></Select>
              <Button type="primary">开始录入</Button>
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
        <div>
          <img src="{{ url_for('video_feed') }}" width="640" height="480"></img>
        </div>
      </div>
    );
  }, []);


  return (
    <div className={css.allBox}>
      <p className={css.leftTitle}>人脸识别系统</p>
      <div className={css.container}>
        {renderLeft()}
        {renderImage()}
        <RightStatus name="叶墨沫" isSmile={true} isUnique={true}></RightStatus>
      </div>
    </div>
  );
};
export default App;
