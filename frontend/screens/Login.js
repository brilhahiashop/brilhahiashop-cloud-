import React, {useState} from 'react';
import { View, TextInput, Button, Text } from 'react-native';
import { api } from '../services/api';

export default function Login({navigation}){
  const [email,setEmail]=useState('');
  const [password,setPassword]=useState('');
  const [err,setErr]=useState('');

  async function submit(){
    try{
      const r = await api.post('/auth/login',{email,password});
      if(r.data && r.data.token){
        // store token later - for demo proceed to dashboard
        navigation.replace("Dashboard");
      } else {
        setErr("Login falhou.");
      }
    }catch(e){
      setErr("Login falhou.");
    }
  }

  return (
    <View style={{padding:20,marginTop:100}}>
      <Text style={{fontSize:30,marginBottom:20,color:'#00b7ff'}}>BRILHAH IA SHOP</Text>
      <TextInput placeholder="Email" style={{borderWidth:1,padding:10,marginBottom:10}} onChangeText={setEmail}/>
      <TextInput placeholder="Password" secureTextEntry style={{borderWidth:1,padding:10,marginBottom:10}} onChangeText={setPassword}/>
      <Button title="Entrar" onPress={submit}/>
      {err ? <Text style={{color:'red'}}>{err}</Text>:null}
    </View>
  );
}
