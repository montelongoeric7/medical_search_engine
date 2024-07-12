import React from 'react';
import { Box, Text } from '@chakra-ui/react';

const Footer = () => {
  return (
    <Box bg="teal.500" p={4} mt={4} color="white" textAlign="center">
      <Text>&copy; 2024 Medical Search Engine. All rights reserved.</Text>
    </Box>
  );
};

export default Footer;
