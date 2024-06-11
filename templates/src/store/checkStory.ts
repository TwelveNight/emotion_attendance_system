import {StateCreator, StoreApi, create} from 'zustand';
import {createJSONStorage, persist} from 'zustand/middleware';
import {immer} from 'zustand/middleware/immer';
import { Draft } from 'immer';


type setDraftState<State> = (fn: (state: Draft<State>)=>void) => void

const statePersistFactor = <State, Action>(
  key: string,
  state: State,
  action: (set: setDraftState<State>) => Action,
) => {
  return create(
    persist(
      immer<State & Action>(set => ({
        ...state,
        ...action(set),
      })),
      {
        name: key,
        storage: createJSONStorage(() => localStorage),
      },
    ),
  );
};
export interface Story{
  userId:string,
  time:string,
  emotion:string,
}
interface State {
  checkStoryList:Story[]
}
interface Action{
  addCheckStory:(story:Omit<Story,'time'>)=>void

}

const useCheckStoryStore = statePersistFactor<State , Action>('checkStory', {
  checkStoryList:[],
},(set)=>({
  addCheckStory:(story:Omit<Story,'time'>)=>{
    set((state)=>{
      state.checkStoryList.push({
        ...story,
        // MM-DD HH-MM-SS 形式
        time:new Date().toLocaleString().split(' ')[0]+' '+new Date().toLocaleString().split(' ')[1]
      })
    })
  },

}))
export default useCheckStoryStore