import React from 'react';
import { Box, Heading, Image, VStack, HStack, Text } from '@chakra-ui/react';
import eventImage1 from '../assets/logo.png'; // Ensure you have these images in the assets folder
import eventImage2 from '../assets/logo.png';
import eventImage3 from '../assets/logo.png';

const Events = () => {
  return (
    <Box textAlign="center" py={10} px={6}>
      <Heading as="h1" size="2xl" mb={6}>
        Upcoming Events and Information !
      </Heading>
      <Text fontSize="lg" mb={10}>
        Check out our exciting upcoming events!!!
      </Text>
      <HStack spacing={10} justify="center" wrap="wrap">
        <VStack>
          <Image
            src={eventImage1}
            alt="Event 1"
            borderRadius="lg"
            boxSize="250px"
            mb={4}
          />
          <Text fontSize="md" fontWeight="bold">Event 1</Text>
          <Text fontSize="sm" color="gray.600">Placeholder for info regarding event #1</Text>
        </VStack>
        <VStack>
          <Image
            src={eventImage2}
            alt="Event 2"
            borderRadius="lg"
            boxSize="250px"
            mb={4}
          />
          <Text fontSize="md" fontWeight="bold">Event 2</Text>
          <Text fontSize="sm" color="gray.600">Placeholder for info regarding event #2</Text>
        </VStack>
        <VStack>
          <Image
            src={eventImage3}
            alt="Event 3"
            borderRadius="lg"
            boxSize="250px"
            mb={4}
          />
          <Text fontSize="md" fontWeight="bold">Event 3</Text>
          <Text fontSize="sm" color="gray.600">Placeholder for info regarding event #3 three</Text>
        </VStack>
      </HStack>
    </Box>
  );
};

export default Events;
