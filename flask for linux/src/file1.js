/**
 * @api {Post} https://www.lvyingzhao.cn/dianfei
 * @apiGroup 接口
 *
 * @apiParam {String} home 宿舍楼
 * @apiParam {String} num  门号
 * @apiParamExample {json} Request-Example
 * {
 *  "home": "梅2楼"
 *  "num":"B4222"
 * }
 *
 * @apiSuccessExample  {json} Response-Example
 * {
 *   "status": "200",
 *   "msg": "ok"
 *   "data": "["227.43"]"
 * }
 */
function getUserInfo(username) {
  // 假如这个函数是根据用户名返回用户信息的
}