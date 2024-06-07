import { FC, useCallback } from "react";
import css from "./index.module.css";

interface StatusTableType {
  userStatusInfoList: UserStatusInfoType[];
}

const StatusTable: FC<StatusTableType> = ({ userStatusInfoList = [] }) => {
  const renderList = useCallback(() => {
    return userStatusInfoList.map((item, index) => {
      return (
        <div key={index} className={css.tabItem}>
          <div className={css.name}>{item.name}</div>
          <div className={css.times}>{item.times}</div>
          <div className={css.isSmile}>{item.isSmile ? "微笑" : "非微笑"}</div>
          <div className={css.emotions}>
            {item.emotions ? "高兴" : "不高兴"}
          </div>
        </div>
      );
    });
  }, []);
  return (
    <div className={css.tabBox}>
      <div className={css.tabInnerBox}>
        <div className={css.tabItemTop}>
          <div
            style={{
              flex: 1,
            }}
            className={css.topItem}
          >
            用户名
          </div>
          <div
            style={{
              flex: 2,
            }}
            className={css.topItem}
          >
            识别时间
          </div>
          <div
            style={{
              flex: 1,
            }}
            className={css.topItem}
          >
            微笑状态
          </div>
          <div
            style={{
              flex: 1,
            }}
            className={css.topItem}
          >
            表情
          </div>
        </div>
        {renderList()}
      </div>
    </div>
  );
};
export default StatusTable;
