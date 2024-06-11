import { FC, useRef } from 'react'
import css from './index.module.css'
import success from '../../image/success.svg'
import Lottie from 'lottie-web'
import faceAnimation from './animation/face.json'
import useShowAnimation from '../../hook/useShowAnimation'
interface RightStatusType{
  name:string
  isUnique:boolean,
  emotion:string,
    frame:string,
}
const RightStatus:FC<RightStatusType> = ({
  isUnique = false,
  name = "默认用户",
  emotion = "默认", frame = ''
})=>{
  const lottieRef = useRef<HTMLDivElement>(null)
  useShowAnimation(lottieRef,true,300,faceAnimation)


  return (
    <div className={css.rightBox}>
      <div className={css.usernameBox}>当前用户:{name}</div>
      {frame != '' 
      ? 
      <img src={frame} style={{
          width: 200,
      }}></img>
      : <div className='lottie-box' id='lottie-animation' ref={lottieRef} style={{
        width: 200,
        height: 200,
      }}></div>}
      <div className={css.faceStatus}>
        <p>当前人脸识别状态:</p>
        {isUnique?'成功':'失败'}
      </div>
      <div className={css.emotionStatus}>
        <p>当前人物情绪:</p>
        {emotion}
      </div>
      <div className={css.actionStatus}>
        {(isUnique && 
        <div className={css.okBox}>
          <img src={success} style={{
            width: 20,
          }}></img>
             打卡成功 
        </div>
        )
        }
      </div>
    </div>
  )
}

export default RightStatus

