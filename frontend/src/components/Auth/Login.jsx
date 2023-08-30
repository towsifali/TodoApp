import React from 'react'
import {Flex,useColorModeValue,Heading, FormControl, FormErrorMessage, Input, Button} from '@chakra-ui/react'
import {useForm} from 'react-hook-form'
import { useNavigate } from 'react-router-dom'
import ThemeToggler from '../Theme/ThemeToggler'

const Login = () => {
    const  {
        handleSubmit,
        register,
        formState: {errors, isSubmitting}
    } = useForm();
    const navigate = useNavigate()
    const onSubmit = (value) =>{
        console.log(value)
    }
    return (
    <Flex height="100vh" align="center" justifyContent="center">   
        <Flex 
        direction="column" 
        alignItems="center" 
        background={useColorModeValue("gray.100","gray.700")}
        p={12}
        rounded={6}>
            <Heading mb={6}>Login</Heading>
            <form onSubmit={handleSubmit(onSubmit)}>
                <FormControl isInvalid={errors.email}>
                    <Input 
                        placeholder="Email"
                        background={useColorModeValue("gray.300","gray.600")}
                        type ="email"
                        size="lg"
                        mt={6}
                        {...register("email", {
                            required: "This is a required field",
                        })}
                    />
                    <FormErrorMessage>
                        {errors.email && errors.email.message}
                    </FormErrorMessage>
                </FormControl>
                <FormControl isInvalid={errors.password}>
                    <Input 
                        placeholder="Password"
                        background={useColorModeValue("gray.300","gray.600")}
                        type ="password"
                        size="lg"
                        mt={6}
                        {...register("password", {
                            required: "This is a required field",
                        })}
                    />
                    <FormErrorMessage>
                        {errors.password && errors.password.message}
                    </FormErrorMessage>
                </FormControl>
            </form>
            <Button isLoading={isSubmitting} loadingText= "Logging in" width="100%" colorScheme = "green" variant="outline" mt={6} mb={6} type="submit">Login</Button>
            <ThemeToggler showLabel/>
            <Button onClick={() => navigate("/register",{replace:true})} width="100%" colorScheme = "gray" variant="outline" mt={6}>Register</Button>
        </Flex>
    </Flex>
  )
}

export default Login