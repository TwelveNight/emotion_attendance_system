import { useEffect } from "react"

import Lottie from 'lottie-web'
const useShowAnimation = (ref: React.RefObject<HTMLElement>, show: boolean = true, duration: number = 300,animation:string) => {
  useEffect(()=>{
    let ani = Lottie.loadAnimation({
      container: ref.current!,
      renderer: 'svg',
      loop: true,
      autoplay: show,
      animationData: animation
    });
    
  },[])
}
export default useShowAnimation