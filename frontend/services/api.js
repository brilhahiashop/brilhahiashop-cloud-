import axios from 'axios';
import Constants from 'expo-constants';

export const api = axios.create({
  baseURL: Constants.expoConfig?.extra?.backendUrl || Constants.manifest?.extra?.backendUrl || 'https://REPLACE_WITH_BACKEND_URL'
});
