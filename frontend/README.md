BRILHAH Mobile (frontend)
-------------------------
- Update app.json extra.backendUrl with the backend URL after backend is deployed.
- Install dependencies:
  npm install
- Start in tunnel mode (works on phone with Expo Go):
  npx expo start --tunnel
- To build APK in cloud (EAS) you'll need an Expo account and to configure EAS.
  A GitHub Actions workflow is included (../.github/workflows/eas-android-build.yml) to create builds automatically when you push to main and set secrets.
