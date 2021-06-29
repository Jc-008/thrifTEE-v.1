import React from 'react';
import { Container } from "@chakra-ui/react"
import { Grid, GridItem } from "@chakra-ui/react"
import { Heading } from "@chakra-ui/react"
import { Text } from "@chakra-ui/react"
import { Box } from "@chakra-ui/react"
import { DeleteIcon } from '@chakra-ui/icons'
import './OrderConfirmation.css'


export default function ItemDetail({ product }) {
    return (
        <>
            <Grid className="product-details-grid">
                <Grid templateColumns="repeat(4, 1fr)" gap={4}>
                    <GridItem colSpan={1}>{product.name}</GridItem>
                    <GridItem className="img-contain" colSpan={1}>
                        <img src={product.image_url}></img>
                    </GridItem>
                    <GridItem>${product.regular_price}</GridItem>
                    <GridItem><DeleteIcon>Remove</DeleteIcon></GridItem>
                </Grid>
            </Grid>
        </>

    )
}
