declare module '*.module.css' {
  const classes: { [key: string]: string }
  export default classes
}
declare module '*.svg' {
  const src: string
  export default src
}

declare module '*.json' {
  const value: any
  export default value
}