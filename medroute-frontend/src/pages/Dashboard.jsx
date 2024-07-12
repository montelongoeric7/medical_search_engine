import React from 'react';
import { Box, Heading, Image, Button, VStack } from '@chakra-ui/react';
import { useNavigate } from 'react-router-dom';
import arrow from '../assets/arrow.png'; // Ensure the path is correct

const Dashboard = () => {
  const navigate = useNavigate();

  return (
    <Box textAlign="center" py={10} px={6}>
      <Heading as="h2" size="xl" mb={6}>
        Welcome to Your Dashboard
      </Heading>
      <p>Here you can manage your information and other activities. There are a few key features you can. Look below...</p>
      <Image
        src={arrow}
        alt="Arrow pointing down"
        mx="auto"
        mb={6}
        mt={6}
      />
      <VStack spacing={4}>
        <Button
          colorScheme="teal"
          bg="teal.400"
          _hover={{ bg: 'teal.500' }}
          rounded="full"
          onClick={() => navigate('/update')}
        >
          Update Data
        </Button>
        <Button
          colorScheme="teal"
          bg="teal.400"
          _hover={{ bg: 'teal.500' }}
          rounded="full"
          onClick={() => navigate('/search')}
        >
          Search
        </Button>
        <Button
          colorScheme="teal"
          bg="teal.400"
          _hover={{ bg: 'teal.500' }}
          rounded="full"
          onClick={() => navigate('/searchfree')}
        >
          Quick Search !!!! 
        </Button>
      </VStack>
    </Box>
  );
};

export default Dashboard;
