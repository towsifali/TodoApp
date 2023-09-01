import { BrowserRouter as Router, Routes, Route,Navigate} from 'react-router-dom'
import Login from './components/Auth/Login';
import Register from './components/Auth/Register';
import { AuthProvider, AuthConsumer} from './context/JWTContext';
import { Flex, Spinner } from '@chakra-ui/react';
import { PublicRoute } from './components/Auth/PublicRoute';
import { Authenticated } from './components/Auth/Authenticated';

function App() {
  return (
    <>
    <AuthProvider>
      <Router>
        <AuthConsumer>
          {(auth) => !auth.isInitialized ? (
            <Flex
              height="100vh"
              alignItems="center"
              justifyContent="center"
              >
                <Spinner
                  thickness='4px'
                  speed='0.65s'
                  emptyColor='green.200'
                  color='green.500'
                  size="xl"
                />
              </Flex>
          ): (
              <Routes>
                <Route path="/login" element={<PublicRoute><Login/></PublicRoute>}/>
                <Route path="/register" element={<PublicRoute><Register/></PublicRoute>}/>
                <Route path="/" element={<Authenticated><h1>I am Home</h1></Authenticated>}/>
                <Route path="*" element={<Navigate to="/" />}/>
              </Routes>
          )}
        </AuthConsumer>
      </Router>
      </AuthProvider>
    </>
  );
}

export default App;
