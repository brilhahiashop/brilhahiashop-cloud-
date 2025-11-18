import React, {useEffect} from 'react';
import { ImageBackground } from 'react-native';

export default function Splash({navigation}){
  useEffect(()=>{
    setTimeout(()=>navigation.replace("Login"),1200);
  },[]);
  return <ImageBackground source={require('../assets/splash.png')} style={{flex:1}}/>;
}
